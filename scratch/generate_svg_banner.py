import os
import math
import random

# Generate stylized SVG for Creation of Adam Hands (Human Logic <-> Generative AI)

svg_content = """<svg width="100%" height="280" viewBox="0 0 800 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Glow -->
    <radialGradient id="bg-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F7FF" stop-opacity="0.12" />
      <stop offset="60%" stop-color="#8b5cf6" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#020617" stop-opacity="0" />
    </radialGradient>

    <!-- Hand Gradients -->
    <linearGradient id="left-hand-grad" x1="0%" y1="50%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.2"/>
      <stop offset="70%" stop-color="#0ea5e9" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00F7FF" stop-opacity="1"/>
    </linearGradient>

    <linearGradient id="right-hand-grad" x1="100%" y1="50%" x2="0%" y2="50%">
      <stop offset="0%" stop-color="#6d28d9" stop-opacity="0.2"/>
      <stop offset="70%" stop-color="#8b5cf6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="1"/>
    </linearGradient>

    <linearGradient id="spark-line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F7FF" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#00F7FF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.2"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="intense-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur1" />
      <feGaussianBlur stdDeviation="3" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .spark-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Fira Code', 'Courier New', monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
    }
    
    .hand-left {
      stroke: url(#left-hand-grad);
      stroke-width: 2.2;
      fill: none;
      filter: url(#neon-glow);
    }
    
    .hand-right {
      stroke: url(#right-hand-grad);
      stroke-width: 2.2;
      fill: none;
      filter: url(#neon-glow);
    }

    .flow-dash {
      stroke: url(#spark-line-grad);
      stroke-width: 2;
      stroke-dasharray: 6, 6;
      animation: dashMove 1s linear infinite;
    }

    .pulse-core {
      animation: corePulse 1.6s ease-in-out infinite alternate;
    }

    .particle-dust {
      animation: dustDrift 2.5s ease-in-out infinite;
    }

    .particle-dust-delayed {
      animation: dustDrift 3.2s ease-in-out infinite 0.8s;
    }

    .particle-dust-fast {
      animation: dustDriftFast 1.8s ease-in-out infinite 0.3s;
    }

    @keyframes dashMove {
      from { stroke-dashoffset: 24; }
      to { stroke-dashoffset: 0; }
    }

    @keyframes corePulse {
      0% { transform: scale(0.85); opacity: 0.7; }
      100% { transform: scale(1.35); opacity: 1; }
    }

    @keyframes dustDrift {
      0% { transform: translate(0, 0) scale(1); opacity: 0.9; }
      50% { transform: translate(12px, -8px) scale(1.3); opacity: 0.5; }
      100% { transform: translate(25px, -18px) scale(0.2); opacity: 0; }
    }

    @keyframes dustDriftFast {
      0% { transform: translate(0, 0) scale(1); opacity: 1; }
      100% { transform: translate(-20px, 15px) scale(0.1); opacity: 0; }
    }
  </style>

  <!-- Ambient Dark Background Card -->
  <rect width="800" height="280" rx="16" fill="#030712" />
  <rect width="800" height="280" rx="16" fill="url(#bg-glow)" />

  <!-- Outer Border Frame -->
  <rect x="1" y="1" width="798" height="278" rx="15" stroke="#1e293b" stroke-width="1.5" />

  <!-- HEADER LABELS -->
  <g transform="translate(0, 45)">
    <!-- Left Label (Human Logic) -->
    <circle cx="120" cy="0" r="4" fill="#0ea5e9" filter="url(#neon-glow)"/>
    <text x="135" y="4" fill="#38bdf8" class="spark-text">HUMAN LOGIC</text>

    <!-- Center Badge -->
    <rect x="340" y="-12" width="120" height="24" rx="12" fill="#0f172a" stroke="#00F7FF" stroke-opacity="0.4" stroke-width="1"/>
    <text x="400" y="4" fill="#00F7FF" class="spark-text" text-anchor="middle" font-size="9">CREATION OF AI</text>

    <!-- Right Label (Generative AI) -->
    <text x="665" y="4" fill="#c084fc" class="spark-text" text-anchor="end">GENERATIVE AI</text>
    <circle cx="680" cy="0" r="4" fill="#8b5cf6" filter="url(#neon-glow)"/>
  </g>

  <!-- LEFT HAND (ADAM / HUMAN) - Cyan Neon Vector Contour -->
  <g class="hand-left">
    <!-- Forearm & Wrist -->
    <path d="M 0 210 Q 70 195 120 185 T 180 170" />
    <path d="M 0 250 Q 80 230 135 210 T 195 190" />
    
    <!-- Palm & Back of Hand -->
    <path d="M 180 170 C 210 160 235 150 260 148 C 280 146 295 150 310 152" />
    <path d="M 195 190 C 220 188 245 185 270 180 C 285 178 300 172 315 165" />
    
    <!-- Thumb (pointing up/right) -->
    <path d="M 230 158 C 245 145 260 135 275 130 C 285 127 292 132 285 142 C 275 150 262 155 250 160" />

    <!-- Index Finger (Extending toward center x=372, y=140) -->
    <path d="M 310 148 C 328 144 348 141 372 140" />
    <path d="M 315 154 C 332 150 350 147 372 143" />
    <!-- Fingertip curve -->
    <path d="M 372 140 C 375 141 375 142 372 143" />

    <!-- Middle Finger (Slightly bent) -->
    <path d="M 312 158 C 330 158 348 159 360 162 C 365 163 362 167 355 167 C 342 166 325 164 314 162" />

    <!-- Ring Finger (Curled) -->
    <path d="M 305 165 C 322 168 338 172 348 177 C 352 179 348 182 340 181 C 328 179 312 174 300 170" />

    <!-- Pinky Finger (Curled) -->
    <path d="M 295 172 C 310 178 325 184 335 190 C 338 192 334 195 326 193 C 314 189 298 181 290 176" />
  </g>

  <!-- RIGHT HAND (GOD / GENERATIVE AI) - Purple Cybernetic Vector Contour -->
  <g class="hand-right">
    <!-- Forearm & Wrist -->
    <path d="M 800 210 Q 730 195 680 185 T 620 170" />
    <path d="M 800 250 Q 720 230 665 210 T 605 190" />

    <!-- Palm & Back of Hand -->
    <path d="M 620 170 C 590 160 565 150 540 148 C 520 146 505 150 490 152" />
    <path d="M 605 190 C 580 188 555 185 530 180 C 515 178 500 172 485 165" />

    <!-- Thumb -->
    <path d="M 570 158 C 555 145 540 138 525 135 C 515 133 510 138 518 145 C 528 152 540 156 550 160" />

    <!-- Index Finger (Extending toward center x=428, y=140) -->
    <path d="M 490 148 C 472 144 452 141 428 140" />
    <path d="M 485 154 C 468 150 450 147 428 143" />
    <!-- Fingertip curve -->
    <path d="M 428 140 C 425 141 425 142 428 143" />

    <!-- Middle Finger -->
    <path d="M 488 158 C 470 156 450 155 435 156 C 428 157 430 161 438 162 C 452 163 470 163 482 162" />

    <!-- Ring Finger -->
    <path d="M 495 165 C 478 166 460 168 448 171 C 442 173 445 176 453 176 C 465 175 482 172 498 170" />

    <!-- Pinky Finger -->
    <path d="M 505 172 C 490 176 473 180 462 184 C 457 186 460 189 468 188 C 480 186 498 180 508 176" />
  </g>

  <!-- SPARK ENERGY BRIDGE & GAP DUST PARTICLES -->

  <!-- Flowing Energy Line between Fingertips (372, 141.5) to (428, 141.5) -->
  <path d="M 372 141.5 L 428 141.5" class="flow-dash" filter="url(#neon-glow)" />

  <!-- Center Energy Core Spark -->
  <g transform-origin="400 141.5" class="pulse-core">
    <circle cx="400" cy="141.5" r="4" fill="#00F7FF" filter="url(#intense-glow)" />
    <circle cx="400" cy="141.5" r="10" fill="#00F7FF" fill-opacity="0.25" filter="url(#neon-glow)" />
    <circle cx="400" cy="141.5" r="18" fill="#8b5cf6" fill-opacity="0.1" />
  </g>

  <!-- Left Fingertip Node -->
  <circle cx="372" cy="141.5" r="3" fill="#00F7FF" filter="url(#neon-glow)" />

  <!-- Right Fingertip Node -->
  <circle cx="428" cy="141.5" r="3" fill="#c084fc" filter="url(#neon-glow)" />

  <!-- DISSOLVING DUST PARTICLES (Left - Cyan floating right/up) -->
  <g class="particle-dust">
    <circle cx="365" cy="138" r="1.8" fill="#00F7FF" opacity="0.8" />
    <circle cx="355" cy="145" r="1.2" fill="#38bdf8" opacity="0.6" />
    <circle cx="345" cy="135" r="2.2" fill="#0ea5e9" opacity="0.7" />
    <circle cx="330" cy="148" r="1.5" fill="#00F7FF" opacity="0.5" />
    <circle cx="320" cy="132" r="1.0" fill="#38bdf8" opacity="0.4" />
  </g>

  <g class="particle-dust-delayed">
    <circle cx="370" cy="144" r="1.5" fill="#00F7FF" opacity="0.9" />
    <circle cx="360" cy="132" r="2.0" fill="#38bdf8" opacity="0.7" />
    <circle cx="340" cy="142" r="1.2" fill="#0ea5e9" opacity="0.6" />
    <circle cx="325" cy="152" r="1.8" fill="#00F7FF" opacity="0.4" />
  </g>

  <!-- DISSOLVING DUST PARTICLES (Right - Purple floating left/down) -->
  <g class="particle-dust-fast">
    <circle cx="435" cy="138" r="1.8" fill="#c084fc" opacity="0.8" />
    <circle cx="445" cy="145" r="1.2" fill="#8b5cf6" opacity="0.6" />
    <circle cx="455" cy="135" r="2.2" fill="#d946ef" opacity="0.7" />
    <circle cx="470" cy="148" r="1.5" fill="#c084fc" opacity="0.5" />
    <circle cx="480" cy="132" r="1.0" fill="#8b5cf6" opacity="0.4" />
  </g>

  <g class="particle-dust">
    <circle cx="430" cy="144" r="1.5" fill="#c084fc" opacity="0.9" />
    <circle cx="440" cy="132" r="2.0" fill="#8b5cf6" opacity="0.7" />
    <circle cx="460" cy="142" r="1.2" fill="#d946ef" opacity="0.6" />
    <circle cx="475" cy="152" r="1.8" fill="#c084fc" opacity="0.4" />
  </g>
</svg>
"""

with open(r"d:\Github profile\patkaryash\output\creation-hands.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("SVG creation-hands.svg generated successfully.")
