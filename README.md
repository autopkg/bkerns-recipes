bkerns-recipes
--------------

####EMCSyncplicity

Download, JSS, Munki, and Pkg recipes for EMC Syncplicity client. Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that copies first-run files into place to prevent admin prompting and disables software update check and notifications.

####EMCSyncplicitySSO

Exact same functionality as the standard Synplicity client recipes (above), but downloads the SSO client instead of Standard (slightly different).


####Microsoft Office 2016

JSS recipes for MS Word, Excel, PowerPoint, Outlook, and OneNote updates that reference the download recipes in the "recipes" repo. 

####Microsoft OneNote

A JSS recipe for Microsoft OneNote app from the App Store.

####StuffIt

A Pkg recipe for StuffIt Expander that references keelysam's download recipe.

####TechSmithCamtasia

Download, JSS, Munki, and Pkg recipes for TechSmith Camtasia.

Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that sets a number of first-run preferences. Also, the postinstall uses the optional CAMTASIA_KEY input value to key the install with your registration key, if desired.

To use CAMTASIA_KEY, create an override and add the key value. The needed key value can be pulled from a machine that has already been registered with the following:

```
cp /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key.plist
defaults read /Users/Shared/TechSmith/Camtasia/Camtasia\ Registration\ Key.plist RegKey | sed 's/[<> ]//g'
```

####TechSmithSnagit

Download, JSS, Munki, and Pkg recipes for TechSmith Snagit.

Munki and Pkg recipes include a preinstall script that removes an existing version prior to install, and a postinstall script that sets a number of first-run preferences. Also, the postinstall uses the optional SNAGIT_KEY input value to key the install with your registration key, if desired.

To use SNAGIT_KEY, create an override and add the key value. The needed key value can be pulled from a machine that has already been registered with the following:

```
cp /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey.plist
defaults read /Users/Shared/TechSmith/Snagit/SnagitRegistrationKey.plist RegKey | sed 's/[<> ]//g'
```


*NOTE: I previously used Munki regularly, but have recently moved to a JAMF shop. I have provided Munki recipes that I believe should work, but I do not make use of them. Munki Admins, please let me know if a Munki recipe needs adjusted!*

bkerns-recipes
--------------