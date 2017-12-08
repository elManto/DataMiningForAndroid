# DataMiningForAndroid
Applciation of data mining techniques to classify Android malware and goodware

Approach 1: Check the frequency of the opcodes that belong to every app in the dataset.
            This is not so good because for 2000 apk only 2 instructions are common
            to every app.

Approach 2: Look at flow instruction. This is better than the previosu, but there is not
            correlation with is_malware or not

Approach 3: Group the flow instructions into macro group

They conclude that
using 2gram the detection ratio is quite low, achieving a
maximum value of 69.66%, thus 2-grams do not seem
to be appropriate for malware detection. They achieved
best results for detection ratio using 4grams, getting a
maximum detection ratio of 91.25%. For the following
n values, detection ratio is lower than for n = 4, however,
the second best results are achieved with n = 8.
