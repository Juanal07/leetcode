/**
 * @param {number} x
 * @return {number}
 */
const reverse = (x) => {
  let str = String(x);
  let result = "";
  for (let i = 1; i <= str.length; i++) {
    result = result + str[str.length - i];
  }
  if (result.at(-1) === "-") {
    result = result.at(-1).concat(result);
    result = result.slice(0, -1);
  }
  result = Number(result);
  if (result >= Math.pow(2, 31) - 1 || result <= -1 * Math.pow(2, 31)) {
    return 0;
  }
  return result;
};

console.log(reverse(234));
