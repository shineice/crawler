const request = require('request');
const cheerio = require('cheerio');
const fs = require("fs");


const earthquake = function () {
  request({
    url: "https://www.wayfair.com/furniture/sb0/beds-c46122.html", // 中央氣象局網頁
    method: "POST"
  }, function (error, response, body) {
    if (error || !body) {
      return;
    }
  const $ = cheerio.load(body);
  let result = [];
  const table = $('.ProductCardReviews-container');

  for (let i=1; i<table.length;i++){
    const time= table.eq(i).text();
    result.push(Object.assign({time}));
  }
  console.log(result);
  fs.writeFileSync("result.json",JSON.stringify(result));
  });
};

earthquake();
