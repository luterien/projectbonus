
// Login form inputs

var userIdInput = $('#id_username');
userIdInput.addClass('login-field');
userIdInput.attr('placeholder','Enter your name')
userIdInput.parent().find('label').removeClass('fui-lock-16');
userIdInput.parent().find('label').addClass('fui-man-16');

var userPassInput = $('#id_password');
userPassInput.addClass('login-field');
userPassInput.attr('placeholder','Password')

// Register form inputs

var userMailInput = $('#id_email');
userMailInput.addClass('login-field');
userMailInput.attr('placeholder','E-Mail Adress');
userMailInput.parent().find('label').removeClass('fui-lock-16');
userMailInput.parent().find('label').addClass('fui-mail-16');

var userPassInputRg = $('#id_password1');
userPassInputRg.addClass('login-field');
userPassInputRg.attr('placeholder','Password')

var userPassInputRg2 = $('#id_password2');
userPassInputRg2.addClass('login-field');
userPassInputRg2.attr('placeholder','Password (Again)')