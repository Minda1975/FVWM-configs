# FVWM
My FVWM configs and other stuff which fits into a common style.

This is personal FVWM window manager configuration files, plus other useful stuff.

What is FVWM? FVWM is an extremely powerful ICCCM-compliant multiple virtual desktop window manager for the X Window system. Originally a twm derivative, FVWM has evolved into a powerful and highly configurable environment for Unix-like systems. 

All FVWM configuration is in .fvwm. This include config file with key bindings, colors, start up programs etc. There are also directories with scripts, icons, images and catche for thumbnails.

Also, i put configs for Also, i put configs for ranger fm (with trash support, package  [trash-cli](https://github.com/andreafrancia/trash-cli#can-i-alias-rm-to-trash-put) is needed), mpd, ncmpcpp (a simple ncmpcpp config, with album art support. To use ncmpcpp with album art, simply launch ncmpcpp -c /home/yourusername/.config/ncmpcpp/config-art-dark. Urxvt with pixbuf enabled is needed. Also integrated with dunst notification. Just copy my dunst config, install dunst, and do nothing. Dunst will launch automatically if triggered by notify-send event), xresources (my configuration for URxvt, including copy paste support. Hit Alt+C to copy, and Alt+V to paste (xsel package is needed). I put the colour configuration in ~/.xrdb folder and include it in Xresources using #include command. It makes me able to change or mix the colour scheme for urxvt and rofi easily. You will understand if you look at it. All of my favourite terminal colour scheme i frequently use on my setup is available in ~/.xrdb/color folder), scrot+viewnior (a simple script to take screenshoot using scrot, then add date to the file name, then open the result instantly using Viewnior), urxvt (draw a floating URxvt), rofi (rofi colour is set in ~/.Xresources, but it just an #INCLUDE command. The actual colour configuration is in ~/.xrdb/rofi. You will understand if you look at it. And the launch configuration is in .fvwm/cripts dir.
Also i included scripts for capturing videos of your dektop (in .utility folder). So you don't need any external program. You just need ffmpeg and mkv codec, mostly autoinstalled when You have a multimedia player like Smplayer. To use this, just launch the sript `record`.

The video will be saved in ~/Videos/record.mkv. Rename it first before take another recording session 😉
To stop recording, just navigate to script `stop-recording` and launch it.
 
My prefered IDE is Geany, so i included Geany config and color schemes that relevant to the overall picture.

In this repo you will find Gtk2/3 themes (Fantome, Lumiere, Noita, Ocha, Tee, Vestica, Charma-Nightingale, Charma-Ype, Forest-Dark, Forest-Darker and Forest-Light) and icons (Arc, Canta, ePapirus, Numix, Numix-Circle, Numix-Circle-Light, Numix-Light, Papirus, Papirus-Adapta, Papirus-Adapta-Nokto, Papirus-Dark and Papirus-Light). These themes and icons are very relevant to the overall picture.

Bash is my default terminal, so it’s very appealing to get the best out of it.  Running a Git command without knowing the current branch is like running rm or mkdir in the terminal without knowning the current directory. It is dangerous and error-prone. So i use [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt).

Screens:
![Screenshot](screen.png?raw=true "Clear")
![Screenshot](screen_1.png?raw=true "Notification")
![Screenshot](screen_2.png?raw=true "Rofi")
![Screenshot](screen_3.png?raw=true "Binclock")
![Screenshot](screen_4.png?raw=true "Terms")
![Screenshot](screen_5.png?raw=true "Apps")
![Screenshot](screen_6.png?raw=true "Icons")
![Screenshot](screen_7.png?raw=true "Geany")
![Screenshot](screen_8.png?raw=true "Bash")
![Screenshot](screen_9.png?raw=true "Fakefetch")
![Screenshot](screen_10.png?raw=true "Pokemon")
