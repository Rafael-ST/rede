const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './assets/js/index.js',
  output: {
    filename: 'main.bundle.js',
    path: path.resolve(__dirname, 'static/assets/js'),
    publicPath: '/static/assets/js/',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader, // Extrai o CSS em um arquivo separado
          'css-loader', 
          'sass-loader'
        ],
      },
    ],
  },
  plugins: [
    new CopyWebpackPlugin({
      patterns: [
        { from: path.resolve(__dirname, 'assets/images'), to: path.resolve(__dirname, 'static/images') },
      ],
    }),
    new MiniCssExtractPlugin({ // Adiciona o plugin MiniCssExtractPlugin
      filename: 'css/custom.css', // Nome e diretório do arquivo CSS gerado
    }),
  ],
  devServer: {
    static: {
      directory: path.join(__dirname, 'static'),
    },
    hot: true,
    compress: true,
    port: 9000,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    devMiddleware: {
      writeToDisk: true,
    },
  },
  mode: 'development',
};
