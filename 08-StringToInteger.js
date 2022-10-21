/**
 * @param {string} s
 * @return {number}
 */
// TODO
const myAtoi = (s) => {
  result = "";
  let isNegative = false;
  let i = 0;
  // trim zeros
  while (s[i] === "0") {
    console.log("cero");
    i++;
  }
  for (i; i < s.length; i++) {
    let char = s[i];
    console.log("for", s[i]);
    if (char === "+") {
      continue;
    }
    if (char === "-") {
      isNegative = true;
      continue;
    }
  }
  return result;
};

console.log(myAtoi("00042"));
