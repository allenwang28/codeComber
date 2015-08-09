#! /bin/bash

cat > comb << EOF1
#!/usr/bin/env python
import sys
sys.path.insert(0, '$(pwd)')
import comber 

c = comber.Comber()
c.run()
EOF1

cat > uncomb << EOF1
#!/usr/bin/env python
import sys
sys.path.insert(0, '$(pwd)')
import uncomber 

u = uncomber.Uncomber()
u.run()
EOF1

chmod +x comb
chmod +x uncomb
mv comb /usr/local/bin
mv uncomb /usr/local/bin
