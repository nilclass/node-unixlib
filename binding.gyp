{
  "targets": [
    {
      "target_name": "unixlib",
      "include_dirs": [ "security/pam_appl.h" ],
      "link_settings": {
        "libraries": [ "-lpam" ]
      },
      "conditions": [
		[ "OS=='win'", {
		
		}, { # OS != win
          "cflags": [ "-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall" ]
        }
      ] ],
      "sources": [ "unixlib.cc" ]
    }
  ]
}
