$('a.clickable').click(function() {
  console.log("activert!");
  console.log(this.href);
  $.get(this.href);
  return false;
});
