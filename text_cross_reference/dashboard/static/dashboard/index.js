// Keep this for reference but is not necessary

document
  .getElementsByName("text-search-1")[0]
  .addEventListener("keyup", highlight);

function highlight() {
  console.log(this.value);
  let textElement = document.getElementById("text-1");
  let textToSearch = textElement.innerHTML;
  let regularExpression = new RegExp(`${this.value}`, "gi");
  console.log(regularExpression);

  let unHighlightText = textToSearch
    .replaceAll(`<mark>`, ``)
    .replaceAll(`</mark>`, "");

  // TODO: is there a way to retain capitalization? or do I need a whole different approach?
  //let foundWord = unHighlightText.match(regularExpression)[0];
  let highlightedText = unHighlightText.replace(
    regularExpression,
    `<mark>${this.value}</mark>`
  );

  textElement.innerHTML = highlightedText;
}
