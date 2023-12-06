import { useState, useEffect } from 'react';
import { DateRange } from 'react-date-range';
import { TextField, Button } from '@mui/material';
import format from 'date-fns/format';
import 'react-date-range/dist/styles.css';
import 'react-date-range/dist/theme/default.css';

const Calendario = ({ onChange }) => {
  const [dateRange, setState] = useState([{ startDate: null, endDate: null, key: 'selection' }]);
  const [previousRange, setPreviousRange] = useState({ startDate: null, endDate: null });
  const [isCalendarVisible, setIsCalendarVisible] = useState(false);
  const [activeInput, setActiveInput] = useState('startDate');

  const handleSelect = (ranges) => {
    const updatedRange = { ...dateRange[0] };
    if (activeInput === 'startDate') {
      updatedRange.startDate = ranges.selection.startDate;
    } else {
      updatedRange.endDate = ranges.selection.endDate;
    }
    setState([updatedRange]);
    setIsCalendarVisible(false);
  };
  useEffect(() => {
    const newRange = {
      from: dateRange[0].startDate ? format(dateRange[0].startDate, 'yyyy-MM-dd') : null,
      to: dateRange[0].endDate ? format(dateRange[0].endDate, 'yyyy-MM-dd') : null,
    };

    if (newRange.from !== previousRange.startDate || newRange.to !== previousRange.endDate) {
      onChange(newRange);
      setPreviousRange({ startDate: newRange.from, endDate: newRange.to });
    }
  }, [dateRange, onChange, previousRange]);

  const handleClean = () => {
    setState([{ startDate: null, endDate: null, key: 'selection' }]);
    setPreviousRange({ startDate: null, endDate: null });
    onChange({ from: null, to: null });
  };

  return (
    <div style={{display:'flex'}}>
      <TextField
        label="Fecha Inicio"
        type="text"
        value={dateRange[0].startDate ? format(dateRange[0].startDate, 'MM/dd/yyyy') : ''}
        onClick={() => {setIsCalendarVisible(true); setActiveInput('startDate');}}
        readOnly
      />
      <TextField
        label="Fecha Fin"
        type="text"
        value={dateRange[0].endDate ? format(dateRange[0].endDate, 'MM/dd/yyyy') : ''}
        onClick={() => {setIsCalendarVisible(true); setActiveInput('endDate');}}
        readOnly
      />
      <div style={{ position: 'relative' }}>
        {isCalendarVisible && (
          <div style={{ position: 'absolute', zIndex: 1000, top:'60px', right: '120px'}}>
            <DateRange
              className="custom-date-range"
              onChange={handleSelect}
              ranges={dateRange}
              direction="horizontal"
            />
            <Button style={{ position: 'absolute', width: '180px', bottom:'-20px', left: '0', background: 'white'}} onClick={() => setIsCalendarVisible(false)}>Cerrar Calendario</Button>
          </div>
        )}
      </div>
      <Button onClick={handleClean}>Limpiar fechas</Button>
    </div>
  );
};

export default Calendario;
