/* 

GOAL : Given a certain level of heat resource & production, electrical resource & prodction, 
and which generation you are in, can you reach max level tempearture? 

Future TODOS:
- Which generation will you reach max temperature? (When can you shift your focus?)
- Depending on your income, can you supplement using Standard Projects (i.e. buying an Asteroid to raise temperature?)

# Given a certain heat_resource, production, generation, will you reach max temperature by final generation?

*/

// Other Constants

import chalk from 'chalk'; // Make colors for consoel
const log = console.log

// Constsants for game
const maxTemp = 8
const startTemp = -30
let maxGeneration = 12; // Can be 12 or 14 depending on game type
const tempSteps = 19; // number of steps required to get max temperature
const heatRequired = 152; // Amount of Heat required to get max heat
const heatAdvance = 8; // Heat required to advance a level of temperature

let curTemp = startTemp; // Intialize temp at start of the game, unless otherwise noted

let defaultData = {
    'heatRes' : 0, // Heat Resource
    'heatProd' : 0, // Heat Production
    'elecRes' : 0, // Electrical Resource
    'elecProd' : 0, // Electrical Production
    'heatGenerated' : 0, // Total amount of heat generation
    'curTemp' : -30, // Current Temperature
    'curGeneration' : 1 // current generation
}

export function HeatCaclcuator(data, maxGeneration){
    /* 
    Using electrical and heat production, track how much heat is generation at current level of production
    If there is enough heat to increase temperature, do it
    Then show current resources 
    */
   for (let i = data.curGeneration; i <= maxGeneration; i++) {

   }
}

export function NextGeneration(data) {
    /* Convert electrity to heat, produce resources, add to heatGenerated */
    data.curGeneration++;
    console.log('\n',`===New Generation==${data.curGeneration}`, '\n');
    data.heatRes += data.elecRes; // Convert excess electricity into heat
    data.elecRes = data.elecProd // Produce electricity
    data.heatRes += data.heatProd // Produce heat production into heat
    data.heatGenerated += data.heatRes // Overall heat generated
    PrintResources(data)
}

export function PrintResources(data) {
    log(chalk.magenta(`Elec Prod: ${data.elecProd} - ` +  chalk.red(`Heat Prod: ${data.heatProd}`)))
    log(chalk.magenta(`Elec Res:  ${data.elecRes} - ` +  chalk.red(`Heat Res: ${data.heatRes}`)))
    log(`Heat Generated: ${data.heatGenerated}`)
}

export function AsteroidHit(data) {
    if (data.heatRes >= heatAdvance) {
        while (data.heatRes >= heatAdvance) {
            data.curTemp+=2;
            if (data.curTemp == -24 || -20) { // Increase heatProd if hit -24 or -20
                data.heatProd++;
                log(chalk.red(`Heat Prod Increase! : ${data.heatProd-1} -> ${data.heatProd}`))
            }
            data.heatRes -= heatAdvance;
            log('Asteroid Hit -',chalk.red(` Current Temp: ${data.curTemp}`))
        }
    } else {
        log(chalk.yellow('Not enough heat, skip'))
    }
}

let testData = {
    'heatRes' : 24,
    'heatProd' : 3,
    'elecRes' : 3,
    'elecProd' : 0,
    'heatGenerated' : 0,
    'curTemp' : -26,
    'curGeneration' : 1
}

AsteroidHit(testData);
