const CLIENT_ID = 'YOUR_CLIENT_ID.apps.googleusercontent.com'; // INPUT_REQUIRED {Enter your Client ID here}
const SCOPES = 'https://www.googleapis.com/auth/gmail.modify';
const REDIRECT_URI = 'YOUR_REDIRECT_URI'; // INPUT_REQUIRED {Enter your Redirect URI here}

function getAuthToken() {
  return new Promise((resolve, reject) => {
    chrome.identity.getAuthToken({ interactive: true }, function(token) {
      if (chrome.runtime.lastError) {
        reject(chrome.runtime.lastError);
      } else {
        resolve(token);
      }
    });
  });
}

function revokeToken(token) {
  return new Promise((resolve, reject) => {
    chrome.identity.removeCachedAuthToken({ token }, function() {
      const xhr = new XMLHttpRequest();
      xhr.open('GET', `https://accounts.google.com/o/oauth2/revoke?token=${token}`);
      xhr.send();
      resolve();
    });
  });
}

window.getAuthToken = getAuthToken;
window.revokeToken = revokeToken;