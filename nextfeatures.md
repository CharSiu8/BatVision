yFeatures to add after MVP:

1.5
✅ Confidence score — Show % certainty of prediction
✅ Add more batmans — kilmer, clooney, keaton
    ⚠️ Still need to add more images. The model is not sufficient for deployment yet and needs more data of these 3 batmans. 
        - need Data Augmentation. crop full face/mask. train model on the mask crop as well as its full context photo
✅ Agentic AI gets box office stats for the movie of the specific batman in that photo
✅ Agentic AI gets a random quote of that specific batman actor

Current Deployed Model Stats:
affleck, bale, niteowl, darkwing, and pattinson
Precision - 90.4 -- Recall - 90.4 -- AP - 95.7

Iteration 7 with clooney, kilmer, keaton added stats: NOT READY
Precision - 82.8% -- Recall - 80.0 -- AP- 83.7

2.0 Possibilites
Side-by-side comparison — Display reference image next to uploaded image
Multi-image batch upload — Classify multiple images at once
Voice narration — Eleven Labs reads out the result
Explain prediction — Highlight facial features model used (Grad-CAM)
Reverse search — Agent finds similar images online
API endpoint — Let others call your classifier programmatically
Fine-tuning interface — User corrects wrong predictions, model improves
