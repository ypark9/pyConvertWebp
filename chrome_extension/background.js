chrome.contextMenus.create({
    title: "Download Image as PNG",
    contexts: ["image"],
    onclick: function(info, tab) {
      chrome.downloads.download({url: info.srcUrl, filename: "image.png"});
    }
  });
  
  chrome.contextMenus.create({
    title: "Download Image as JPG",
    contexts: ["image"],
    onclick: function(info, tab) {
      var canvas = document.createElement("canvas");
      var ctx = canvas.getContext("2d");
      var img = new Image();
      img.crossOrigin = "anonymous";
      img.onload = function() {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        var dataURL = canvas.toDataURL("image/jpeg");
        chrome.downloads.download({url: dataURL, filename: "image.jpg"});
      };
      img.src = info.srcUrl;
    }
  });
  
  chrome.contextMenus.create({
    title: "Download Image as GIF",
    contexts: ["image"],
    onclick: function(info, tab) {
      chrome.downloads.download({url: info.srcUrl, filename: "image.gif"});
    }
  });
  