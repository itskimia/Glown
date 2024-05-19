const express = require('express');
const router = express.Router();
const db = require('../db');

// Example route to get all products
router.get('/products', (req, res) => {
  const sql = 'SELECT * FROM products';
  db.all(sql, [], (err, rows) => {
    if (err) {
      res.status(400).json({ error: err.message });
      return;
    }
    res.json({
      message: 'success',
      data: rows
    });
  });
});

// Example route to add a product
router.post('/products', (req, res) => {
  const { name, price } = req.body;
  const sql = 'INSERT INTO products (name, price) VALUES (?, ?)';
  const params = [name, price];
  db.run(sql, params, function (err) {
    if (err) {
      res.status(400).json({ error: err.message });
      return;
    }
    res.json({
      message: 'success',
      data: { id: this.lastID, name, price }
    });
  });
});

module.exports = router;