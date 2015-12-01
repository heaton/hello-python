var $ = function(q) {return document.querySelector(q)};

function User(user, pass, state) {
  return {
    user: user,
    pass: pass,
    state: state
  };
}

var Users = {
  user1: User('user1', 'pass1', 'normal'),
  user2: User('user2', 'nop', 'normal'),
  user3: User('user3', 'pass3', 'locked')
};
  
function check() {
  var u = $('#user').value;
  var p = $('#pass').value;
  var user = findUser(u, p);
  if (user && user.state == 'normal') {
    location.href = 'main.html';
  } else if (user && user.state == 'locked') {
    $('#message').innerHTML = 'This account has been locked!';
  } else {
    $('#message').innerHTML = 'Wrong username or password!';
  }
}

function findUser(u, p) {
  return Users[u] && Users[u].pass == p ? Users[u] : null;
}
