import { useState, useEffect } from 'react';
import Calendario from './Calendario';
import { FormGroup, FormControlLabel, Checkbox, Button } from '@mui/material';

const Form = ({ onChange }) => {
    const [filter, setFilter] = useState({
        isGbaEnabled: false,
        birthDate: {
            from: null,
            to: null,
        }
    });

    useEffect(() => {
        onChange(filter);
    }, [filter]);


    return (
        <div style={{ display: 'flex', width: '100%' }}>
        <FormGroup row style={{ display: 'flex', width: '100%', justifyContent: 'flex-end', alignItems: 'center' }}>
           <FormControlLabel
                    control={<Checkbox onChange={(e) => setFilter({...filter, isGbaEnabled: e.target.checked})} />}
                    label="Es de GBA"
                />
                <Calendario onChange={(value) => setFilter({...filter, birthDate: value})} />
            </FormGroup>
        </div>
    );
}

export default Form;
