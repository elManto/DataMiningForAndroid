# DataMiningForAndroid

Applciation of data mining techniques to classify Android malware and goodware

Approach 1: Check the frequency of the opcodes that belong to every app in the dataset.
            This is not so good because for 2000 apk only 2 instructions are common
            to every app.

Approach 2: Look at flow instruction. This is better than the previosu, but there is not
            correlation with is_malware or not.

Approach 3: Group the flow instructions into macro group.

The 3rd approach allow us to reach an accuracy of 75%


