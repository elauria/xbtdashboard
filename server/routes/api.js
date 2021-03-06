const express = require("express");
const router = express.Router();

const exchanges_controller = require("../controllers/exchangesController");
const ohlcv_controller = require("../controllers/ohlcvController");
const chart_library_controller = require("../controllers/chartLibraryController");

// exchange routes

router.get("/exchange/bitmex", exchanges_controller.bitmex);
router.get("/exchange/bitfinex", exchanges_controller.bitfinex);
router.get("/exchange/binance", exchanges_controller.binance);
router.get("/exchange/okex", exchanges_controller.okex);
router.get("/exchange/coinbase", exchanges_controller.coinbase);

// ohlcv

router.get("/ohlcv/:tf", ohlcv_controller.ohlcv);
router.get("/oi/:exchange/:symbol", ohlcv_controller.openInterest);
router.get("/liquidations/:exchange/:symbol", ohlcv_controller.liquidations);

// chart library

router.get(
  "/chartlib/configurationData",
  chart_library_controller.configuration_data_get
);
router.get("/chartlib/exchanges", chart_library_controller.exchanges_get);

module.exports = router;
