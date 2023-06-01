'use strict';

const ns = {
  'win32': 'win',
  'darwin': 'mac'
};

if (process.platform in ns) {
  module.exports = require('bindings')(ns[process.platform]);
} else {
  throw new Error(`Unsupported platform: ${process.platform}`);
}
