const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

module.exports = async function (context, req) {
    const results = [];
    const filePath = path.join(__dirname, 'data.csv'); // Asegúrate de tener el CSV aquí
    fs.createReadStream(filePath)
      .pipe(csv())
      .on('data', (data) => results.push(data))
      .on('end', () => {
          context.res = {
              headers: { "Content-Type": "application/json" },
              body: results
          };
      });
};

