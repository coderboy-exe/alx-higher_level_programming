#!/usr/bin/node

if ((process.argv[2] === undefined) || (isNaN(process.argv[2]))) {
	console.log('1');
} else {
	let num = (parseInt(process.argv[2]));

	while (num >= 1) {
		num = num * (num - 1);
		num -= 1;
	}
	console.log(num);
}
