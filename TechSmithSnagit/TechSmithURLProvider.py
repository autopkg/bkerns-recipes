#!/usr/bin/python

import urllib
import json

from autopkglib import Processor, ProcessorError


__all__ = ["TechSmithURLProvider"]

TS_BASE_URL = "https://www.techsmith.com/api/v/1/products/getallversions/%s"
TS_VER_URL = "https://www.techsmith.com/api/v/1/products/getversioninfo/%s"
TS_DL_URL = "http://download.techsmith.com%s%s"

class TechSmithURLProvider(Processor):
    """Provides URL to the latest Techsmith product release."""
    description = __doc__
    input_variables = {
        "product_name": {
            "required": True,
            "description":
                "Product to fetch URL for. One of 'camtasia' or 'snagit'.",
        },
        "base_url": {
            "required": False,
            "description": "Default is '%s." % TS_BASE_URL,
        },
    }
    output_variables = {
        "url": {
            "description": "URL to the latest Techsmith product release.",
        },
    }

    def main(self):
        """Provide a Techsmith download URL"""
        product_name = self.env["product_name"]
        base_url = self.env.get("base_url", TS_BASE_URL)
        if product_name == "camtasia":
            prodcode = "9"
        elif product_name == "snagit":
            prodcode = "100"
        url = base_url % (prodcode)
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        vers = "%s.%s.%s" % (data[0]["Major"], data[0]["Minor"], data[0]["Maintenance"])
        versionid = data[0]["VersionID"]
        vurl = TS_VER_URL % (versionid)
        vresponse = urllib.urlopen(vurl)
        vdata = json.loads(vresponse.read())
        dlurl = TS_DL_URL % (vdata["PrimaryDownloadInformation"]["RelativePath"], vdata["PrimaryDownloadInformation"]["Name"])
        self.env["url"] = dlurl
        self.env["version"] = vers
        self.output("Found URL %s" % self.env["url"])
        self.output("Found Version %s" % self.env["version"])


if __name__ == "__main__":
    PROCESSOR = TechSmithURLProvider()
    PROCESSOR.execute_shell()

