# dedupe-raw-images
A simple and slightly dangerous script that removes jpg copies of raw images

## Motivation
I use a Samsung Galaxy S7 and like to shoot my pictures in raw. However, the S7 forces you to save both a jpg and a dng for every picture you take in raw. This is a slightly dangerous script that removes the jpgs that have a corresponding dng file and keeps the jpgs that don't have a raw counterpart.

Side note: I think the S7 has one of the best cameras on a smartphone, but its post processing is particularly crappy since it ups the contrast and sharpens way too much. And to add to the trouble, you can only save in raw if you are in the pro mode, but you can't set the pro mode as the default mode to use when opening the app. Unless you make a shortcut on a home screen, but then you can't use the double tap shortcut, which is super useful for when you want to capture something really quickly. _Why you do this, Samsung??_ So I end up with some pictures that aren't shot in raw and some that are, and going through the trouble of checking which jpgs are safe to delete is lame, so I make a computer do it for me =P

## Usage
Clone the repo or copy the `dedupe` file, whatever you need to do to get the code. I'm not super familiar with publishing Python packages so I haven't put it up anywhere else yet. 

**Important**: This makes the assumption that a jpg and a dng are the same if they have the same filename minus the extension. It doesn't do any fancy magic to check otherwise. This script currently only handles jpg and dng file formats. If you want to use it for other formats, it'll require a few minor edits. It also doesn't really do any error checking yet and removes files permanently. I've also only tried it on OSX El Capitan and with Python 2.7, so be careful when using it!

Or if you like to live on the edge, you can #believe it'll work and run this command:

```
python dedupe.py <file path to directory>
```

If you get an error about `no such file or directory`, try using an unescaped file path. I think `os.listdir` does some conflicting magic. I might look into it. Or you can too!

## Contributing
I very quickly scrapped this together and there are definitely a lot of potential issues that may arise. If you know how to address any of them, especially with error handling/making this less dangerous, please send in a PR!
