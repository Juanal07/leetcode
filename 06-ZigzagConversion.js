/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = (s, numRows) => {
  if (numRows === 1) {
    return s;
  }
  let rows = [];
  for (let i = 0; i < numRows; i++) {
    rows[i] = "";
  }
  for (let i = 0; i < s.length; i++) {
    let row = i % (numRows + numRows - 2);
    if (row >= numRows) {
      row = numRows + numRows - 2 - row;
    }
    rows[row] = rows[row] + s[i];
  }
  return rows.join("");
};

console.log(convert("PAYPALISHIRING", 4));
console.log(convert("A", 1));
