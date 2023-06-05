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
        ["OS=='mac' and target_arch=='x64'", {
          "target_name": "mac-x64",
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
        ["OS=='mac' and target_arch=='arm64'", {
          "target_name": "mac-arm64",
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
        ["OS=='win' and target_arch=='x64'", {
          "target_name": "win-x64",
          "sources": [
            "./src/main.cpp"
          ]
        }],
        ["OS=='win' and target_arch=='arm64'", {
          "target_name": "win-arm64",
          "sources": [
            "./src/main.cpp"
          ]
        }],
        ["OS=='win' and target_arch=='ia32'", {
          "target_name": "win-ia32",
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