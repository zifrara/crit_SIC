 #!/bin/sh

~/bin/nautyCOLOR/listg -qe ex.g6 |   sed -e 's/\ \ /\n/g' | sed -e 's/\ /\n/1' | sed -e 's/^0\ /31\ /g'
