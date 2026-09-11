const path = require('path');

module.exports = {
    entry: './firebase-config.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    mode: 'production',
};
