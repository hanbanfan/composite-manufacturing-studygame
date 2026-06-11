from pathlib import Path
import re

path = Path("index.html")
html = path.read_text()

# Remove academic integrity warning block
html = re.sub(
    r'\s*<div class="warning">\s*<strong>Academic integrity:</strong>.*?</div>',
    '',
    html,
    flags=re.S
)

# Make header friendlier
html = html.replace(
    "A clear study dashboard for composite manufacturing, materials, processes, testing, repair, and exam practice.",
    "Learn composite materials step by step with study guides, flashcards, quizzes, calculators, process practice, and exam review."
)

# Add better dashboard cards and study priority section
html = html.replace(
    '''<div class="success">
          <h3>Best daily study loop</h3>
          <ol>
            <li>Read one book chapter study path.</li>
            <li>Review the matching study guide.</li>
            <li>Do 10 flashcards out loud.</li>
            <li>Take one quiz round.</li>
            <li>Use Process Lab once.</li>
            <li>Write one note in “My Notes.”</li>
          </ol>
        </div>''',
    '''<div class="success">
          <h3>Best daily study loop</h3>
          <ol>
            <li><strong>Start with Book Study Path:</strong> read one chapter card.</li>
            <li><strong>Use Study Guides:</strong> review the matching explanation.</li>
            <li><strong>Flashcards:</strong> do 10 cards out loud.</li>
            <li><strong>Quiz Mode:</strong> take one 10-question quiz.</li>
            <li><strong>Process Lab:</strong> solve one manufacturing scenario.</li>
            <li><strong>My Notes:</strong> write one sentence in your own words.</li>
          </ol>
        </div>

        <div class="study-box">
          <h3>What to study first</h3>
          <ol>
            <li>Matrix vs. reinforcement</li>
            <li>Fiber types: glass, carbon, aramid/Kevlar</li>
            <li>Thermosets vs. thermoplastics</li>
            <li>Anisotropy and fiber orientation</li>
            <li>Manufacturing process selection</li>
            <li>Voids, porosity, wet-out, and quality assurance</li>
            <li>Damage assessment and repair</li>
            <li>Safety, environmental, and factory operations</li>
          </ol>
        </div>'''
)

# Add nav button for checklist
html = html.replace(
    '<button onclick="showSection(\'exam\', this)">Exam Review</button>\n      <button onclick="showSection(\'notes\', this)">My Notes</button>',
    '<button onclick="showSection(\'exam\', this)">Exam Review</button>\n      <button onclick="showSection(\'checklist\', this)">Concept Checklist</button>\n      <button onclick="showSection(\'notes\', this)">My Notes</button>'
)

# Add checklist section before notes
checklist_section = r'''
      <section id="checklist">
        <h2>Master Concept Checklist</h2>
        <p class="muted">Use this to make sure you are not missing anything important before quizzes, labs, the midterm, presentations, or the final.</p>

        <div class="grid">
          <div class="card">
            <h3>Core Concepts</h3>
            <ul>
              <li>Composite definition</li>
              <li>Constituents, phases, and interface</li>
              <li>Matrix vs. reinforcement</li>
              <li>PMC, MMC, and CMC</li>
              <li>Advantages and disadvantages of composites</li>
              <li>Specific strength and specific modulus</li>
              <li>Anisotropy and fiber orientation</li>
            </ul>
          </div>

          <div class="card">
            <h3>Fibers and Reinforcements</h3>
            <ul>
              <li>Glass fiber: cost and corrosion resistance</li>
              <li>Carbon fiber: stiffness, strength, and low density</li>
              <li>Aramid/Kevlar: impact resistance</li>
              <li>Boron and ceramic reinforcements</li>
              <li>Continuous vs. chopped fibers</li>
              <li>Fiber length, orientation, shape, and material</li>
              <li>Fabrics, mats, whiskers, flakes, and particulates</li>
            </ul>
          </div>

          <div class="card">
            <h3>Matrix Materials</h3>
            <ul>
              <li>Matrix functions</li>
              <li>Thermosets and crosslinking</li>
              <li>Thermoplastics and reheating</li>
              <li>Polyester, vinyl ester, epoxy, phenolic, polyimide</li>
              <li>Metal matrices for higher temperatures</li>
              <li>Ceramic matrices for very high temperatures</li>
              <li>Moisture, solvent, chemical, and temperature limits</li>
            </ul>
          </div>

          <div class="card">
            <h3>Manufacturing Processes</h3>
            <ul>
              <li>Hand layup</li>
              <li>Spray-up</li>
              <li>Vacuum bagging</li>
              <li>Prepreg layup</li>
              <li>Autoclave curing</li>
              <li>RTM / liquid molding</li>
              <li>Pultrusion</li>
              <li>Filament winding</li>
              <li>Compression molding</li>
              <li>Tooling and mold selection</li>
            </ul>
          </div>

          <div class="card">
            <h3>Quality, Testing, and Calculations</h3>
            <ul>
              <li>Density</li>
              <li>Fiber volume fraction</li>
              <li>Void volume ratio / porosity</li>
              <li>Wet-out and dry spots</li>
              <li>Cured laminate quality</li>
              <li>Mechanical testing</li>
              <li>Environmental testing</li>
              <li>Failure testing</li>
              <li>Documentation and process control</li>
            </ul>
          </div>

          <div class="card">
            <h3>Fabrication, Repair, and Safety</h3>
            <ul>
              <li>Cutting, drilling, machining</li>
              <li>Delamination and fiber pull-out</li>
              <li>Adhesive bonding</li>
              <li>Mechanical fasteners and stress concentrations</li>
              <li>Damage detection and assessment</li>
              <li>Repair patches and restored load paths</li>
              <li>PPE, dust, fibers, resin, solvents, ventilation</li>
              <li>EPA/environmental and factory operations</li>
            </ul>
          </div>
        </div>

        <div class="success">
          <h3>Final readiness test</h3>
          <p>You are ready when you can explain each process, name when to use it, name one advantage, name one limitation, and connect it to a fiber/matrix choice.</p>
        </div>
      </section>
'''
html = html.replace('      <section id="notes">', checklist_section + '\n      <section id="notes">')

# Add small UX CSS improvements
html = html.replace(
    '@media (max-width: 850px) {',
    '''
    .card:hover,
    details:hover {
      transform: translateY(-1px);
    }

    .study-box, .success, .warning, .card {
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .flashcard:hover {
      background: #eef2ff;
    }

    #quizFeedback {
      font-size: 1.1rem;
      font-weight: bold;
    }

    @media (max-width: 850px) {'''
)

# Add more concepts to bookPath, guides, flashcards, and quizQuestions before initialization
injection = r'''
    bookPath.push(
      {
        chapter: "Extra Focus: Inspection, Defects, and Quality Problems",
        tags: ["inspection", "defects", "voids", "wet-out", "quality", "testing"],
        study: "Focus on how manufacturing choices create defects and how defects reduce performance.",
        learn: [
          "Poor wet-out can cause dry fibers and weak bonding.",
          "Trapped air can become voids or porosity.",
          "Incorrect cure can reduce matrix performance.",
          "Poor machining can cause delamination and fiber pull-out.",
          "Inspection connects manufacturing quality to real performance."
        ],
        check: "Explain how a void forms and why it can reduce strength."
      },
      {
        chapter: "Extra Focus: Design for Manufacturing",
        tags: ["design", "manufacturing", "process selection", "tooling", "cost"],
        study: "Focus on matching part requirements to material and process instead of memorizing processes separately.",
        learn: [
          "Part shape influences process selection.",
          "Production volume influences process selection.",
          "Fiber orientation must match the load path.",
          "Tooling affects cost, surface quality, and repeatability.",
          "A cheaper material can become expensive if the process is slow or inconsistent."
        ],
        check: "Given a part shape and production volume, justify a process choice."
      }
    );

    guides.push(
      {
        title: "Design for Manufacturing",
        tags: ["design", "manufacturing", "tooling", "cost"],
        body: "A good composite design is not just a material choice. It connects loads, fiber orientation, matrix type, part shape, tooling, cure method, production volume, inspection, cost, and repair. If a part is a tube, filament winding may make sense. If it is a long constant cross-section, pultrusion may make sense. If it is high-performance aerospace, prepreg and autoclave processing may make sense."
      },
      {
        title: "Common Defects",
        tags: ["defects", "voids", "delamination", "wet-out", "quality"],
        body: "Important defects include voids, porosity, dry spots, poor wet-out, delamination, fiber waviness, resin-rich areas, resin-starved areas, contamination, poor cure, machining damage, and bond failure. For exams, connect the defect to a cause and a consequence."
      },
      {
        title: "How to Compare Processes",
        tags: ["process", "manufacturing", "exam"],
        body: "When comparing processes, ask: What shape does it make? Is it open mold or closed mold? Is it low-volume or high-volume? How well does it control fiber orientation? How well does it control resin content? What are the cost and quality tradeoffs? What defects are likely?"
      }
    );

    flashcards.push(
      ["Quality", "What is a dry spot?", "An area where resin did not fully wet the reinforcement."],
      ["Quality", "What is fiber waviness?", "A defect where fibers are not straight or aligned as intended, reducing load-carrying efficiency."],
      ["Quality", "What is a resin-rich area?", "A region with too much resin and not enough reinforcement."],
      ["Quality", "What is a resin-starved area?", "A region with too little resin to properly wet and bind the reinforcement."],
      ["Quality", "Why does cure control matter?", "The matrix needs the correct cure conditions to reach intended properties."],
      ["Manufacturing", "What is open molding?", "A process using an open mold surface, such as hand layup or spray-up."],
      ["Manufacturing", "What is closed molding?", "A process where material is shaped inside a closed mold, such as RTM or compression molding."],
      ["Manufacturing", "Why does tooling matter?", "Tooling affects shape accuracy, surface finish, repeatability, cost, and cure behavior."],
      ["Fabrication", "What is a stress concentration?", "A local area of high stress, often around holes, notches, or fasteners."],
      ["Repair", "What is a scarf repair?", "A tapered repair that increases bonding area and helps restore load transfer."],
      ["Safety", "Why control composite dust?", "Dust and fibers can irritate skin/lungs and may require PPE and ventilation."],
      ["Safety", "Why track environmental regulations?", "Resins, solvents, dust, and waste can create disposal and air-quality concerns."],
      ["Properties", "What is dimensional stability?", "The ability of a material or part to keep its shape and dimensions under service conditions."],
      ["Properties", "What is fatigue resistance?", "Resistance to damage under repeated loading."],
      ["Applications", "Why use composites in wind energy?", "They allow large, lightweight, fatigue-resistant blade structures."],
      ["Applications", "Why use composites in automotive parts?", "Weight reduction, corrosion resistance, styling/formability, and part consolidation."]
    );

    quizQuestions.push(
      q("Quality", "A dry spot is...", ["An area with poor resin wet-out", "An area with perfect cure", "A metal fastener", "A type of fiber"], 0),
      q("Quality", "Fiber waviness usually...", ["Reduces load-carrying efficiency", "Always improves strength", "Removes the matrix", "Means the part is isotropic"], 0),
      q("Quality", "A resin-rich area has...", ["Too much resin compared with reinforcement", "No resin", "Only carbon fiber", "Only ceramic matrix"], 0),
      q("Quality", "A resin-starved area has...", ["Too little resin to wet and bind reinforcement", "Too much resin", "No fibers", "Only paint"], 0),
      q("Manufacturing", "Hand layup and spray-up are examples of...", ["Open molding", "Closed molding only", "Filament winding only", "Pultrusion only"], 0),
      q("Manufacturing", "RTM and compression molding are examples of...", ["Closed molding", "No-mold processing", "Only machining", "Only inspection"], 0),
      q("Manufacturing", "Tooling affects...", ["Shape, surface finish, cost, repeatability, and cure behavior", "Only textbook chapters", "Only fiber color", "Nothing important"], 0),
      q("Fabrication", "A stress concentration can happen around...", ["Holes, notches, and fasteners", "Only flat surfaces", "Only textbooks", "The navigation bar"], 0),
      q("Repair", "A scarf repair is useful because it...", ["Creates a tapered bond area for load transfer", "Removes the need for inspection", "Adds random voids", "Only changes color"], 0),
      q("Safety", "Composite dust control matters because...", ["Dust and fibers can irritate skin/lungs", "Dust always improves strength", "Dust replaces PPE", "Dust makes resin cure faster"], 0),
      q("Applications", "Composite wind turbine blades benefit from...", ["Light weight and fatigue resistance", "High void content", "No matrix", "No inspection"], 0),
      q("Properties", "Dimensional stability means...", ["Keeping shape and dimensions under service conditions", "Changing shape constantly", "Absorbing all moisture", "Having no fibers"], 0)
    );
'''
html = html.replace('    populateDecks();', injection + '\n    populateDecks();')

path.write_text(html)
print("Optimized index.html successfully.")
