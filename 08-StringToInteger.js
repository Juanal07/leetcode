/**
 * @param {string} s
 * @return {number}
 */
const myAtoi = (s) => {
  if (s.length === 0) {
    return 0;
  }

  result = "";

  let isNegative = false;

  // Step 1: Trim whitespaces
  let i = 0;
  while (i < s.length && s[i] === " ") {
    i++;
  }

  // Step 2: Sign
  if (i < s.length && (s[i] === "-" || s[i] === "+")) {
    if (s[i] === "-") {
      isNegative = true;
    }
    i++;
  }

  // Step 3: Number
  while (i < s.length && isNumeric(s[i])) {
    result = result + s[i];
    i++;
  }

  // Step 4: Parse
  if (result === "") {
    return 0;
  }
  result = Number(result);
  if (isNegative) {
    result = result * -1;
  }

  // Check range
  const topRange = Math.pow(2, 31) - 1;
  const bottomRange = -1 * Math.pow(2, 31);
  if (result > topRange) {
    return topRange;
  }
  if (result < bottomRange) {
    return bottomRange;
  }

  return result;
};

function isNumeric(value) {
  return /^-?\d+$/.test(value);
}

console.log(myAtoi("   0004238asdf"));
