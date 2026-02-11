Features to add after MVP:

1.5
✅ Confidence score — Show % certainty of prediction
✅ Agentic AI gets box office stats for the movie of the specific batman in that photo
✅ Agentic AI gets a random quote of that specific batman actor
✅ Add more batmans — kilmer, clooney, keaton
    ⚠️ Still need to add more images. The model is not sufficient for deployment yet and needs more data of these 3 batmans. 
        - need Data Augmentation. crop full face/mask. train model on the mask crop as well as its full context photo
        - need to find more distinguishing features:     
                Keaton = rounder cowl, 1989 style
                Kilmer = sleeker cowl, nipples on suit
                Bale = angular cowl, tactical suit
        - need to curate images with differences
                Remove images where suits look generic
                Keep images with clear cowl/suit details
                Add images showing unique features of each


Current Deployed Model Stats:
affleck, bale, niteowl, darkwing, and pattinson
Precision - 90.4 -- Recall - 90.4 -- AP - 95.7

<img width="914" height="987" alt="Screenshot 2026-02-11 085824" src="https://github.com/user-attachments/assets/66aef285-791b-4007-8546-2ce7de2c40ca" />

Iteration 7 with clooney, kilmer, keaton added stats: NOT READY
Precision - 82.8% -- Recall - 80.0 -- AP- 83.7

<img width="859" height="1079" alt="Screenshot 2026-02-11 085728" src="https://github.com/user-attachments/assets/b94db53d-cbb4-4f68-8c57-ecb787e846cb" />

2.0 Possibilites
Side-by-side comparison — Display reference image next to uploaded image
Multi-image batch upload — Classify multiple images at once
Voice narration — Eleven Labs reads out the result
Explain prediction — Highlight facial features model used (Grad-CAM)
Reverse search — Agent finds similar images online
API endpoint — Let others call your classifier programmatically
Fine-tuning interface — User corrects wrong predictions, model improves
