(() => {
"use strict";

if(typeof flashcards!=="undefined"){
  flashcards.push(
    ["Advanced", "Longitudinal rule of mixtures for elastic modulus?", "E1 = EfVf + EmVm."],
    ["Advanced", "What is Vm if there are only fiber and matrix phases?", "Vm = 1 - Vf."],
    ["Advanced", "Simple inverse rule of mixtures for transverse modulus?", "1/E2 = Vf/Ef + Vm/Em."],
    ["Advanced", "Critical fiber length equation?", "lc = σf d / (2τi)."],
    ["Advanced", "What happens if actual fiber length is much greater than critical length?", "The fiber can develop more of its tensile strength through interfacial load transfer."],
    ["Advanced", "Why does fiber strength often appear lower for longer tested lengths?", "Longer lengths have a greater chance of containing a critical flaw; this is described statistically with Weibull behavior."],
    ["Advanced", "What is a sandwich structure?", "Strong thin face sheets separated by a lightweight core to increase bending stiffness efficiently."],
    ["Advanced", "What does vacuum bagging improve?", "Compaction, removal of trapped air, laminate consolidation, and control of excess resin."]
  );
}

if(typeof quizQuestions!=="undefined" && typeof q==="function"){
  quizQuestions.push(
    q("Advanced","For a two-phase composite, if Vf = 0.65, Vm is...",["0.35","0.65","1.65","0"],0),
    q("Advanced","The longitudinal modulus rule of mixtures is...",["E1 = EfVf + EmVm","E1 = Ef/Em","E1 = Vf + Vm","E1 = ρV"],0),
    q("Advanced","Critical fiber length mainly relates fiber strength, diameter, and...",["Interfacial shear strength","Color","Void percentage only","Panel width"],0),
    q("Advanced","A sandwich core is primarily useful because it...",["Separates face sheets and increases bending stiffness efficiently","Replaces all fibers","Eliminates the matrix","Always increases density"],0),
    q("Advanced","Weibull statistics are useful for brittle fibers because strength is...",["Statistically affected by flaw population and tested length","Always identical","Independent of defects","Only controlled by density"],0)
  );
}

const nav=document.querySelector("nav");
const main=document.querySelector("main");

if(nav && main){
  const button=document.createElement("button");
  button.textContent="Advanced Composites";
  button.onclick=function(){showSection("advanced",button)};
  nav.appendChild(button);

  const section=document.createElement("section");
  section.id="advanced";
  section.innerHTML=`
    <h2>Advanced Composites</h2>
    <p class="muted">
      Mechanics + exam calculations layered onto the existing manufacturing material.
    </p>

    <div class="grid">

      <div class="card">
        <h3>Longitudinal Rule of Mixtures</h3>
        <p>E1 = EfVf + EmVm</p>

        <label>Fiber modulus Ef</label>
        <input id="ac-ef" type="number" step="any">

        <label>Matrix modulus Em</label>
        <input id="ac-em" type="number" step="any">

        <label>Fiber volume fraction Vf (decimal)</label>
        <input id="ac-vf" type="number" step="any">

        <button onclick="advancedROM()">Calculate E1</button>
        <p id="ac-rom-result"></p>
      </div>

      <div class="card">
        <h3>Transverse Modulus</h3>
        <p>1/E2 = Vf/Ef + Vm/Em</p>

        <label>Fiber modulus Ef</label>
        <input id="ac-tef" type="number" step="any">

        <label>Matrix modulus Em</label>
        <input id="ac-tem" type="number" step="any">

        <label>Fiber volume fraction Vf</label>
        <input id="ac-tvf" type="number" step="any">

        <button onclick="advancedTransverse()">Calculate E2</button>
        <p id="ac-trans-result"></p>
      </div>

      <div class="card">
        <h3>Critical Fiber Length</h3>
        <p>lc = σf d / (2τi)</p>

        <label>Fiber tensile strength σf</label>
        <input id="ac-sigma" type="number" step="any">

        <label>Fiber diameter d</label>
        <input id="ac-diameter" type="number" step="any">

        <label>Interfacial shear strength τi</label>
        <input id="ac-tau" type="number" step="any">

        <button onclick="advancedCriticalLength()">Calculate lc</button>
        <p id="ac-lc-result"></p>
      </div>

      <div class="card">
        <h3>Filament Count from Linear Density</h3>
        <p>
          N = λ / (ρA), with consistent units.
        </p>

        <label>Linear mass density λ</label>
        <input id="ac-linear" type="number" step="any">

        <label>Fiber material density ρ</label>
        <input id="ac-rho" type="number" step="any">

        <label>Single-fiber diameter d</label>
        <input id="ac-fd" type="number" step="any">

        <button onclick="advancedFilaments()">Calculate N</button>
        <p id="ac-fil-result"></p>
      </div>

      <div class="card">
        <h3>Weibull Survival</h3>
        <p>S = exp[-(L/L0)(σ/σ0)^m]</p>

        <label>Test length L</label>
        <input id="ac-L" type="number" step="any">

        <label>Reference length L0</label>
        <input id="ac-L0" type="number" step="any">

        <label>Stress σ</label>
        <input id="ac-s" type="number" step="any">

        <label>Reference stress σ0</label>
        <input id="ac-s0" type="number" step="any">

        <label>Weibull modulus m</label>
        <input id="ac-m" type="number" step="any">

        <button onclick="advancedWeibull()">Calculate survival</button>
        <p id="ac-w-result"></p>
      </div>

    </div>

    <div class="study-box">
      <h3>Advanced Exam Checklist</h3>
      <ul>
        <li>Rule of mixtures and assumptions</li>
        <li>Longitudinal vs. transverse loading</li>
        <li>Fiber and matrix volume fractions</li>
        <li>Carbon, glass, and aramid fiber behavior</li>
        <li>Anisotropy and orthotropy</li>
        <li>Critical fiber length and load transfer</li>
        <li>Linear density and filament count</li>
        <li>Weibull strength statistics</li>
        <li>Sandwich face sheets and core</li>
        <li>Impact damage and hidden delamination</li>
        <li>Prepreg, vacuum bagging, and repair</li>
      </ul>
    </div>
  `;
  main.appendChild(section);
}

function val(id){
  const n=Number(document.getElementById(id).value);
  return Number.isFinite(n)?n:null;
}

window.advancedROM=function(){
  const ef=val("ac-ef"), em=val("ac-em"), vf=val("ac-vf");
  const out=document.getElementById("ac-rom-result");
  if(ef===null||em===null||vf===null||vf<0||vf>1){
    out.textContent="Enter Ef, Em, and Vf from 0 to 1.";
    return;
  }
  const vm=1-vf;
  const e=ef*vf+em*vm;
  out.textContent=`Vm = ${vm.toFixed(4)}; E1 = ${ef}(${vf}) + ${em}(${vm.toFixed(4)}) = ${e.toFixed(5)}`;
};

window.advancedTransverse=function(){
  const ef=val("ac-tef"),em=val("ac-tem"),vf=val("ac-tvf");
  const out=document.getElementById("ac-trans-result");
  if(ef===null||em===null||vf===null||ef<=0||em<=0||vf<0||vf>1){
    out.textContent="Enter positive moduli and Vf from 0 to 1.";
    return;
  }
  const vm=1-vf;
  const e=1/(vf/ef+vm/em);
  out.textContent=`Vm = ${vm.toFixed(4)}; E2 = 1/[${vf}/${ef} + ${vm.toFixed(4)}/${em}] = ${e.toFixed(5)}`;
};

window.advancedCriticalLength=function(){
  const s=val("ac-sigma"),d=val("ac-diameter"),tau=val("ac-tau");
  const out=document.getElementById("ac-lc-result");
  if(s===null||d===null||tau===null||tau===0){
    out.textContent="Enter σf, d, and nonzero τi.";
    return;
  }
  const lc=s*d/(2*tau);
  out.textContent=`lc = (${s})(${d})/[2(${tau})] = ${lc.toFixed(6)} in the same length unit used for d.`;
};

window.advancedFilaments=function(){
  const linear=val("ac-linear"),rho=val("ac-rho"),d=val("ac-fd");
  const out=document.getElementById("ac-fil-result");
  if(linear===null||rho===null||d===null||rho<=0||d<=0){
    out.textContent="Enter positive λ, ρ, and d using one consistent unit system.";
    return;
  }
  const area=Math.PI*d*d/4;
  const massPerLength=rho*area;
  const count=linear/massPerLength;
  out.textContent=`Single fiber area = πd²/4 = ${area.toExponential(5)}; N = λ/(ρA) = ${count.toFixed(2)}. Verify your units are consistent.`;
};

window.advancedWeibull=function(){
  const L=val("ac-L"),L0=val("ac-L0"),s=val("ac-s"),s0=val("ac-s0"),m=val("ac-m");
  const out=document.getElementById("ac-w-result");
  if([L,L0,s,s0,m].some(x=>x===null)||L0<=0||s0<=0||m<=0){
    out.textContent="Enter valid positive reference values.";
    return;
  }
  const exponent=(L/L0)*Math.pow(s/s0,m);
  const survival=Math.exp(-exponent);
  out.textContent=`Survival = ${(survival*100).toFixed(3)}%; Failure probability = ${((1-survival)*100).toFixed(3)}%.`;
};

if(typeof populateDecks==="function") populateDecks();
if(typeof populateQuizCategories==="function") populateQuizCategories();

})();
