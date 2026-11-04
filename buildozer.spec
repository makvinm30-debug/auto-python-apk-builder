[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.kolya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.min_api = 21
android.ndk_version = 25b
android.accept_sdk_license = True


[buildozer]
log_level = 2
warn_on_root = 1