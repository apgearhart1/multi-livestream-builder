import {React, useState} from 'react'
import axios from 'axios'
import process_page from './streamExport'
export function GridItem({streamData}) {
    const [streamHTML, setStreamHTML] = useState("");
    const [toggleStream, setToggleStream] = useState(false);
    const handleClick = (url) => {
        axios.get("http://localhost:5000/nba/stream?url=" + url)
            .then(response => {
                console.log(response.data)

                setStreamHTML(response);
                setToggleStream(true);
            })
            .catch(error => {
                console.log(error);
            })
    }
    
    
    
        return (
            <div>
            {!toggleStream && streamData.map((object) => {
                return (
                    <div className="gameSelectorContainer">
                        <button className="gameSelector" onClick={() => handleClick(object.url)}>
                            {object.team1} vs {object.team2}
                        </button>
                    </div>
                )
            })}

            {toggleStream && <div dangerouslySetInnerHTML={{__html: streamHTML}}></div>}
            </div>
        )
    
}
