# Modern UI Redesign

We will completely overhaul the aesthetics of the Health Risk Predictor to look like a premium modern web application (similar to Vercel, Linear, or Stripe).

## User Review Required
Please review this design direction: We will move to a **Dark Mode First** design. The background will feature a deep void/obsidian colour scheme with vibrant, slow-moving "mesh gradients" in the background (glowing orbs of purple, pink, and cyan). The cards will be highly refined frosted glass with 1px semi-transparent borders. 

## Proposed Changes

### UI & Styling
#### [MODIFY] [style.css](file:///c:/Users/Rahul%20Chatterjee/Downloads/antrigravity/static/style.css)
- Implement deep dark background (`#0a0a0a`) with animated radial gradient glowing orbs.
- Upgrade to a 2-column CSS Grid for the form to make it look professional on desktop.
- Add "floating labels" for inputs (labels that slide up when typing).
- Add glowing focus rings and micro-interactions on button hover/click.
- Create a large, glowing circular animated progress indicator for the score.

#### [MODIFY] [index.html](file:///c:/Users/Rahul%20Chatterjee/Downloads/antrigravity/templates/index.html)
- Adjust HTML structure to support floating labels (standard in modern UI).
- Wrap inputs in slightly refined DOM structures to allow for SVG icons inside the inputs.

#### [MODIFY] [result.html](file:///c:/Users/Rahul%20Chatterjee/Downloads/antrigravity/templates/result.html)
- Change the linear bar to an impressive SVG circular progress ring that counts up to the score.
- Stagger animations so results pop in beautifully.

## Verification Plan
1. Start Flask app locally.
2. Verify all CSS transitions and animations render smoothly at 60fps.
3. Provide screenshots/recordings of the final polished look.
