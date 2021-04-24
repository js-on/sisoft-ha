> **It works! This is the default README for this repo. The content is existing but nothing to read has been added, yet.**

# Prerequisites
```sh
git clone https://github.com/js-on/sisoft-ha.git
cd sisoft-ha
pip3 install -r requirements.txt
```

# Usage
## Bash Injection
### Wrong implementation
> You can try Bash injection with this script.

```sh
[js-on@serv ~]$ python3 cmdi_wrong.py
IP: 192.168.1.1; whoami
...
```
### 'Correct' implementation
> This is how to avoid Bash injection

You can do the following to escape any input used as parameters for Bash commands.

```py
import shlex
param = shlex.quote(input("Input: "))
```

```
[js-on@serv ~]$ python3 cmdi_correct.py
IP: 192.168.1.1; whoami
...
```
## SQL Injection
### Wrong implementation
> You can try SQL injection with this script.

```sh
[js-on@serv ~]$ python3 sqli_wrong.py
Mail: " OR ""="
...
```
### 'Correct' implementation
> This is how to avoid SQL injection.

You can do the following to escape any input used as parameters for SQL commands.

```py
SQL = """SELECT * FROM test WHERE mail=?;"""
cursor.execute(SQL, ("asd@asd.de", ))
```

```sh
[js-on@serv ~]$ python3 sqli_correct.py
MAIL: " OR ""="
...
```
## XML Parsing
### Wrong implementation
> You can try a weakened »one million laughs« attack with this script.

```sh
[js-on@serv ~]$ python3 xml_wrong.py
...
Output: lolz
```
### 'Correct' implementation
> This is how to avoid XML parsing issues.

You can do the following to fix common XML parsing issues of the most famous Python XML parsing modules.

```py
from defusedxml.ElementTree import parse, EntitiesForbidden
et = parse("filename.xml")
...
```

```sh
[js-on@serv ~]$ python3 xml_correct.py
...
Error: EntitiesForbidden(...)
```
