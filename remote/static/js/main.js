var currentMode = "youtube";

async function get(url) {
  return await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  }).then(function (response) {
    return response.json();
  }).catch(function (error) {
    console.error(error);
  });
}

function post(url, data) {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then(function (response) {
    response.json();
  }).then(function (data) {
    console.log(data);
  }).catch(function (error) {
    console.error(error);
  });
}

function run(name) {
  post("/api/actions", {"action": {"mode": currentMode, "name": name}});
}

function play() {
  playIcon = document.getElementById('play-icon');
  playIcon.classList.toggle('hidden');

  pauseIcon = document.getElementById('pause-icon');
  pauseIcon.classList.toggle('hidden');

  post("/api/actions", {"action": {"mode": "Youtube", "name": "Play"}});
}

function fullscreen() {
  enterFullscreenIcon = document.getElementById('enter-fullscreen');
  enterFullscreenIcon.classList.toggle('hidden');

  exitFullscreenIcon = document.getElementById('exit-fullscreen');
  exitFullscreenIcon.classList.toggle('hidden');

  post("/api/actions", {"action": {"mode": "Youtube", "name": "Fullscreen"}});
}

function setMode(mode) {
  currentMode = mode.toLowerCase();

  const urlParams = new URLSearchParams(window.location.search);
  urlParams.set('mode', currentMode);
  window.location.search = urlParams;
}

function changeLayout(mode) {
  get("api/actions/" + mode).then(function (response) {
    let actions = response['actions'].map(action => {
      return action['name'].toLowerCase();
    });

    let buttons = document.getElementsByClassName('button');
    for (let i = 0; i < buttons.length; i++) {
      let button = buttons[i];

      if (actions.includes(button.id.toLowerCase().replace("-", ""))) {
        button.classList.remove("hidden");
      } else {
        button.classList.add("hidden");
      }
    }
  });
}

window.addEventListener("load", async function () {
  const url = new URL(window.location.href);
  const mode = url.searchParams.get("mode");
  if (mode) {
    currentMode = mode.toLowerCase();
    changeLayout(mode);
  }

  let modes = await get("api/modes");
  modes = modes['modes'].map(mode => {
    return mode['name'];
  });

  for (let i = 0; i < modes.length; i++) {
    if (modes[i].toLowerCase() == currentMode) {
      const title = document.getElementById('title');
      title.textContent = modes[i];
    }
  }
});
