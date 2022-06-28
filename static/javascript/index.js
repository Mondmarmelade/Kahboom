function redirect(which, input) {
  //which: 0 = name
  //which: 1 = id

  //input: id or name from user
  if (which == 0) {
    input = input.replaceAll(" ", "+");
    input = input.replaceAll("%20", "+");
    window.open("https://kahboom.tk/quizName/" + input, "_self");
  } else if (which == 1) {
    input = input.replace(" ", "");
    window.open("https://kahboom.tk/quizID/" + input, "_self");
  }
}
