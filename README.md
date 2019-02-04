# What is it?
This is a very simple Alfred plugin for Asana.

It allows creating tasks, directly from Aflred

![](.github/2.png)

and to retrieve today's tasks.

![](.github/1.png)

It also integrates with [BitBar](https://getbitbar.com) to show the tasks directly from the status bar.

![](.github/3.png)

# How to install it?

You can download the plugin from [here](https://github.com/lucaquerella/asana-alfred/releases/download/v0.1/Asana.alfredworkflow) and double click to install it.

Once you have it installed, you need to generate an Asana token:

- go to `My Profile Settings`
- then to `Apps`
- then press `Manage Developer Apps`
- and `+ Create New Personal Access Token`

once you have the token, in Alfred type 

> asana token [your token]

for example:

> asana token 0/a4e22334b927bc3f859e70d3341a67a6

and you are ready to go.

### BitBar

If you want to use BitBar integration, you need to download and install BitBar, from its [website](https://getbitbar.com). 
Then you need to create a plugin folder:

> mkdir "~/Library/Application Support/BitBar/scripts"

ensure BitBar uses it:

> defaults write com.matryer.BitBar.plist pluginsDirectory -string "~/Library/Application\ Support/BitBar/scripts"


and link the plugin: 

> ln -s "~/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows/{plugin installation folder}/bitbar.py"

