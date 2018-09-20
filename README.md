# FVWM
My FVWM configs and other stuff which fits into a common style
This is personal FVWM window manager configuration files, plus other useful stuff.

What is FVWM? FVWM is an extremely powerful ICCCM-compliant multiple virtual desktop window manager for the X Window system. Originally a twm derivative, FVWM has evolved into a powerful and highly configurable environment for Unix-like systems. 

All FVWM configuration is in .fvwm. This include config file with key bindings, colors, start up programs etc. There are also directories with scripts, icons, images and catche for thumbnails.

Also, i put configs for mpd, ncmpcpp (a simple ncmpcpp config, with album art support. To use ncmpcpp with album art, simply launch ncmpcpp -c /home/yourusername/.config/ncmpcpp/config-art-dark. Urxvt with pixbuf enabled is needed. Also integrated with dunst notification. Just copy my dunst config, install dunst, and do nothing. Dunst will launch automatically if triggered by notify-send event), xresources (my configuration for URxvt, including copy paste support. Hit Alt+C to copy, and Alt+V to paste (xsel package is needed). I put the colour configuration in ~/.xrdb folder and include it in Xresources using #include command. It makes me able to change or mix the colour scheme for urxvt and rofi easily. You will understand if you look at it. All of my favourite terminal colour scheme i frequently use on my setup is available in ~/.xrdb/color folder), scrot+viewnior (a simple script to take screenshoot using scrot, then add date to the file name, then open the result instantly using Viewnior), urxvt (draw a floating URxvt), rofi (rofi colour is set in ~/.Xresources, but it just an #INCLUDE command. The actual colour configuration is in ~/.xrdb/rofi. You will understand if you look at it. And the launch configuration is in .fvwm/cripts dir.
 
My prefered IDE is Geany, so i included Geany config and color schemes that relevant to the overall picture.

In this repo you will find Gtk2/3 themes (Fantome, Lumiere, Noita, Ocha, Tee and Vestica) and icons (Arc, Canta, ePapirus, Numix, Numix-Circle, Numix-Circle-Light, Numix-Light, Papirus, Papirus-Adapta, Papirus-Adapta-Nokto, Papirus-Dark and Papirus-Light). These themes and icons are very relevant to the overall picture.
All this good is working in Debian 9.5

Screens:
![Screenshot](screen.png?raw=true "Clear")
![Screenshot](screen_1.png?raw=true "Notification")
![Screenshot](screen_2.png?raw=true "Rofi")
![Screenshot](screen_3.png?raw=true "Binclock")
![Screenshot](screen_4.png?raw=true "Terms")
![Screenshot](screen_5.png?raw=true "Apps")
![Screenshot](screen_6.png?raw=true "Icons")
![Screenshot](screen_7.png?raw=true "Geany")
