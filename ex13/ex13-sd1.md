argv needs at least 4 varibles. The first variable is at index 0 and should be the name of the executed script.
From index 1 - 3, the arguments get assigned to the variables first, second and third.
When fewer than 3 arguments are given, argv cannot properly assign the variables and thus it results in a ValueError.
