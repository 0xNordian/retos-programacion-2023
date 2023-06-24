const dict = new Map([
  ["a", "4"],
  ["b", "I3"],
  ["c", "["],
  ["d", ")"],
  ["e", "3"],
  ["f", "|="],
  ["g", "&"],
  ["h", "#"],
  ["i", "1"],
  ["j", ",_|"],
  ["k", ">|"],
  ["l", "1"],
  ["m", "/\\/\\"],
  ["n", "^/"],
  ["o", "0"],
  ["p", "|*"],
  ["q", "(_,)"],
  ["r", "I2"],
  ["s", "5"],
  ["t", "7"],
  ["u", "(_)"],
  ["v", "\\/"],
  ["w", "\\/\\/"],
  ["x", "><"],
]);

function hackerLang(str) {
  const isValidInput = /^[a-zA-Z]+$/.test(str);
  if (isValidInput) {
    return str
      .toLowerCase()
      .split("")
      .map((item) => dict.get(item))
      .join("");
  } else {
    alert("Wrong input, only characters from aA to zZ are valid");
    throw new Error(
      "Wrong input, the user must input only characters from aA to zZ"
    );
  }
}
