/*
for target in `cat targets-443.txt`; do node shot.js https://$target &; done
*/

const colors = require('colors');
const puppeteer = require('puppeteer');
const argv = require('minimist')(process.argv.slice(2));
const file = require('fs');

// CLI Args
const url = argv.url;

(async () => {
  const browser = await puppeteer.launch({ignoreHTTPSErrors: true});
  const page = await browser.newPage();
  
  await page.setViewport({width: 1920, height: 1080});
  try {
    await page.goto(url, { 
        timeout: 5000, // change timeout if you have a slow a f connection
        waitUntil: 'networkidle0'
    });

    await page.waitFor(1000); // set delay for page to load
    
    await page.screenshot({
        path: url.replace(/(^\w+:|^)\/\//, '') + '-screenshot.png',
        fullPage: true
    });
    console.log(url.green);
  
  } catch(e) {
      console.error(e.message.red);
  }
  
  await browser.close();
})();
