import { Grid, Cell } from '@mollycule/lattice'
import './App.css';
import {React, useEffect, useState} from 'react'
import {GridItem} from './GridItem';
import axios from 'axios'
function App() {
  const [streamData, setstreamData] = useState([])
  useEffect(() => {
    var headers= {"Access-Control-Allow-Origin": "*"}

    axios.get('http://localhost:5000/nba', headers)
      .then((response) => response.data)
      .then((jsondata) => {
        console.log(jsondata);
        setstreamData(jsondata);
      })
      .catch((error)=>{
      console.log(error);
   });
  }, []);

  
  
  
  return (
    <div>
      <Grid
      width='1440px'
      mx='auto'
      gap='3px'
      cols={{ lg: 2}}
      rows={{lg: 2}}
      height='730px'
    >
      <Cell y-offset={{ sm: '1', md: '1' }}y-span={{ sm: '1', md: '1' }} className="cell">
        <GridItem streamData={streamData}/>
      </Cell>
      <Cell  y-span={{ sm: '1', md: '1' }}  className="cell">
      <GridItem streamData={streamData}/>
      </Cell>
      <Cell className="cell">
        <GridItem streamData={streamData}/>
      </Cell>
      <Cell x-span={{ sm: '2', md: '1' }}  className="cell">
        <GridItem streamData={streamData}/>
      </Cell>
    </Grid>
    </div>
  );
}

export default App;
