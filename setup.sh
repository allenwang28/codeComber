#! /bin/bash

cat > comb << EOF1
#!/usr/bin/env python
import sys
sys.path.insert(0, '$(pwd)')
import engine

eng = engine.Engine()
eng.run()
EOF1

chmod +x comb
mv comb /usr/local/bin
