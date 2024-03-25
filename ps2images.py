import replicate

output = replicate.run(
  "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
  input={
    "prompt": "pixelated glitchart of close-up of {subject}, ps1 playstation psx gamecube game radioactive dreams screencapture, bryce 3d --style ddCHhSumaNyOrL1Q"
  }
)

print(output)