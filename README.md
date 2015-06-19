bkerns-recipes
--------------

####EMCSyncplicity

Download, Munki, and Pkg recipes for EMC Syncplicity client. Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that copies first-run files into place to prevent admin prompting and disables software update check and notifications.

####EMCSyncplicitySSO

Exact same functionality as the standard Synplicity client recipes, but downloads the SSO client instead of Standard (slightly different).

####StuffIt

A Pkg recipe for StuffIt Expander that references keelysam's download recipe.

####TechSmithCamtasia

Download, Munki, and Pkg recipes for TechSmith Camtasia.

####TechSmithSnagit

Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that sets a number of first-run preferences. Also, the postinstall uses the optional CAMTASIA_KEY input value to key the install with your registration key, if desired.

To use CAMTASIA_KEY, create and override and add the key value. The key value can be gotten from a machine that has already been registered with the following:

```
cp /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key.plist
defaults read "/Users/Shared/TechSmith/Camtasia/Camtasia Registration Key.plist" RegKey | sed 's/[<> ]//g'
```

*NOTE: I previously used Munki regularly, but have recently moved to a JAMF shop. I have provided Munki recipes that I believe should work, but I do not make use of them. Munki Admins, please let me know if a Munki recipe needs adjusted!*

bkerns-recipes
--------------