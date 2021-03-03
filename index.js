var websocket = new WebSocket("ws://localhost:6789");

websocket.onopen = function (event) {
  console.log("websocket opened");
  websocket.send("Test Text");
};

websocket.onmessage = function (event) {
  console.log("Message from websocket ", event.data)
};
