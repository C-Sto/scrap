NB: if your GPU drivers will throttle/you don't care about your hardware:
```
alias hashcat='hashcat --hwmon-disable -w 4'
```

## Extracting hashes from ntds.dit
---
```
python secretsdump.py -user-status -outputfile extracted -system path/to/SYSTEM -ntds path/to/ntds.dit -history LOCAL
```

## Wordlist creation
- I love *x*
```
sed 's/$/i love /g' fnames.txt > ~/wordlists/ilovenames.txt
sed 's/$/i love /g' sportsteams.txt > ~/wordlists/ilovesports.txt
sed 's/$/i love /g' cities.txt > ~/wordlists/ilovecities.txt
cat ~/wordlists/ilove*.txt > love.txt
```

- Create a custom wordlist for the organisation. You can do this however you want. `cewl` can be pretty useful.

- Create a list of usernames
```
cut -d ':' -f 1 extracted.ntds > ~/wordlists/usernames.txt
cut -d ':' -f 1 extracted.ntds | egrep -e '^sa-' -e '^svc-' | sed 's/^sa-//g' | sed 's/^svc-//g' >> ~/wordlists/usernames.txt
```

- Create some wordlists for attacking diceware passwords. Feel free to use a different separator (replace the space in sed with whatever separator you want)
```
sed 's/$/ /g' diceware.txt > diceware1-separators.txt
./combinator.bin diceware1-separators.txt diceware1-separators.txt > diceware2-end-separator.txt
sed 's/ $//g' diceware2-end-separator.txt > diceware2.txt
```

## Quick passes for quick wins
```
hashcat -O -m 1000 extracted.ntds ~/wordlist/love.txt -r ~/rules/5-cleaned.rule 
```
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/usernames.txt -r ~/rules/5-cleaned.rule 
```
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/diceware.txt -r ~/rules/5-cleaned.rule 
```
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/rockyou.txt -r ~/rules/2-medium-InsidePro.rule 
```
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/Top1pt6Million-probable-v2.txt	-r ~/rules/5-cleaned.rule 
```
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/Top2Billion-probable-v2.txt -r ~/rules/1-small-best64.rule 
```
2 word diceware + rules
```
hashcat -O -m 1000 extracted.ntds ~/wordlists/diceware2.txt ~/rules/5-cleaned.rule
```

## Time consuming stuff
3 word diceware
```
hashcat -O -m 1000 extracted.ntds -a 1 ~/wordlists/diceware2-end-separator.txt ~/wordlists/diceware.txt
```

4 word diceware
```
hashcat -m 1000 extracted.ntds -a 1 ~/wordlists/diceware2-end-separator.txt ~/wordlists/diceware2.txt
```

Brute force 8-char
```
hashcat -m 1000 extracted.ntds -a 3 ?a?a?a?a?a?a?a?a --hwmon-disable -w 4
```

Big list, big rules
```
hashcat -m 1000 extracted.ntds ~/wordlists/weakpass2.txt -r ~/rules/5-cleaned.rule
```


## Misc.
Use found passwords as candidates, and use big rules
```
hashcat --show -m 1000 extracted.ntds | cut -d ':' -f 2 > ~/wordlists/cracked-pws.txt && hashcat -m 1000 extracted.ntds ~/wordlists/cracked-pws.txt -r ~/rules/5-cleaned.rule --loopback 
```

## Random (this stuff takes a while)
```
hashcat --show -m 1000 extracted.ntds | cut -d ':' -f 2 > ~/wordlists/cracked-pws.txt
```
```
./generate-rules.bin 500000 $RANDOM > ~/rule/500k-random.rule
```
```
hashcat -m 1000 extracted.ntds ~/wordlists/cracked-pws.txt -r ~/rules/500k-random.rule
```
```
hashcat -m 1000 extracted.ntds ~/wordlists/weakpass2.txt -r ~/rules/500k-random.rule
```
```
shuf ~/wordlists/diceware.txt | pp64.bin --pw-min=9 --elem-cnt-max 10 | hashcat -O -a 0 -m 1000 extracted.ntds -r ~/rules/5-cleaned.rule
```
```
shuf ~/wordlists/diceware.txt | pp64.bin --pw-min=9 --elem-cnt-max 10 | hashcat -O -a 0 -m 1000 extracted.ntds -g 300000
```


## End
Run through cracked passwords with big rules just in case
```
hashcat -m 1000 extracted.ntds ~/wordlists/cracked-pws.txt -r ~/rules/500k-random.rule --loopback
```
