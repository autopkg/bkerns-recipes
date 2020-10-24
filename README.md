bkerns-recipes
--------------

#### EMCSyncplicity

Download, JSS, Munki, and Pkg recipes for EMC Syncplicity client. Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that copies first-run files into place to prevent admin prompting and disables software update check and notifications.

*NOTE: My organization no longer makes use of this product, and as such I am not staying up on its releases. If something changes and the recipe breaks, please let me know.*

#### EMCSyncplicitySSO

Exact same functionality as the standard Synplicity client recipes (above), but downloads the SSO client instead of Standard (slightly different).

*NOTE: My organization no longer makes use of this product, and as such I am not staying up on its releases. If something changes and the recipe breaks, please let me know.*

#### Microsoft OneNote

A JSS recipe for Microsoft OneNote app from the App Store.

*NOTE: This recipe is likely no longer necessary, as there is now a stand-alone app download, and other better recipes out there. I will likely be removing this recipe soon.*

#### StuffIt

A Pkg recipe for StuffIt Expander that references keelysam's download recipe.

#### TechSmithCamtasia

Download, JSS, Munki, and Pkg recipes for TechSmith Camtasia.

Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that sets a number of first-run preferences. Also, the postinstall uses the optional `CAMTASIA_KEY` input value to key the install with your registration key, if desired.

To use `CAMTASIA_KEY`, create an override and
  * For v2020 and newer:
    *  supply your licensing/registation code as the Input Variable's value
  * For v2019 and older:
    * The needed key value can be pulled from a machine that has already been registered with the output following commands:
```
cp /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key\ Unified\ License /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key\ Unified\ License.plist
defaults read /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key\ Unified\ License.plist RegKey | sed 's/[<> ]//g'
```

**[Source](https://support.techsmith.com/hc/en-us/articles/203727638-Camtasia-Mac-Enterprise-Install-Guidelines)**

#### TechSmithSnagit

Download, JSS, Munki, and Pkg recipes for TechSmith Snagit.

Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that sets a number of first-run preferences. Also, the postinstall uses the optional `SNAGIT_KEY` input value to key the install with your registration key, if desired.

To use `SNAGIT_KEY`, create an override and
  * For v2020 and newer:
    *  supply your licensing/registation code as the Input Variable's value
  * For v2019 and older:
    * The needed key value can be pulled from a machine that has already been registered with the output following commands:
```
cp /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey.plist
defaults read /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey.plist RegKey | sed 's/[<> ]//g'
```

**[Source](https://support.techsmith.com/hc/en-us/articles/115007344888-Enterprise-Install-Guidelines-for-Snagit-on-MacOS)**


*NOTE: I previously used Munki regularly, but have recently moved to a JAMF shop. I have provided Munki recipes that I believe should work, but I do not make use of them. Munki Admins, please let me know if a Munki recipe needs adjusted!*

bkerns-recipes
--------------
