{
  "targets": [
    {
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "cflags!": [
        "-fno-exceptions"
      ],
      "cflags_cc!": [
        "-fno-exceptions"
      ],
      "conditions": [
        ["OS=='mac'", {
          "target_name": "mac",
          "sources": [
            "./src/main.mm"  
          ],
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            "MACOSX_DEPLOYMENT_TARGET": "10.7",
            "CLANG_CXX_LIBRARY": "libc++",
            "OTHER_LDFLAGS": [
              "-framework CoreWLAN"
            ],
             "OTHER_CFLAGS": [
              "-ObjC++"
            ]
          }
        }],
        ["OS=='win'", {
          "target_name": "win",
          "sources": [
            "./src/main.cpp"
          ]
        }]
      ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "defines": [
        "_HAS_EXCEPTIONS=1"
      ]
    }
  ]
}