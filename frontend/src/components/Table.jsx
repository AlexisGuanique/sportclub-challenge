import { useEffect, useState } from 'react';
import DataTable from 'react-data-table-component';
import useFetch from '../hooks/useFetch';
import Form from './Form';

const columns = [
    {
        name: 'Nombre',
        selector: row => row.nombre,
    },
    {
        name: 'Apellido',
        selector: row => row.apellido,
    },
    {
        name: 'DNI',
        selector: row => row.dni,
    },
    {
        name: 'Fecha de Nacimiento',
        selector: row => row.fecha_nacimiento,
    },
];

const Table = () => {
    const { get } = useFetch();
    const [tableData, setTableData] = useState([]);

    useEffect(() => {
        const fetchUsers = async () => {
            try {
                const usersData = await get('/usuarios');
                if (usersData?.usuarios?.length) {
                    setTableData(usersData.usuarios);
                } else {
                    throw new Error('User fetch failed');
                }
            } catch (e) {
                console.log(e);
            }
        };

        fetchUsers();
    }, []);

    const searchUsers = async (params) => {
        try {
            // Construcción de la URL de consulta
            const { isGbaEnabled, birthDate: { from: dateFrom, to: dateTo } } = params;
            const queryParams = new URLSearchParams();

            if (dateFrom) queryParams.append('fecha_desde', dateFrom);
            if (dateTo) queryParams.append('fecha_hasta', dateTo);
            if (isGbaEnabled) queryParams.append('localidad_gba', isGbaEnabled);

            const url = `/usuarios/filtrar?${queryParams.toString()}`;

            const usersData = await get(url);
            if (usersData?.usuarios?.length) {
                setTableData(usersData.usuarios);
            } else {
                throw new Error('User fetch failed');
            }
        } catch (e) {
            console.log(e);
        }
    };

    return (
        <>
            <div style={{ padding: '20px', margin:'auto', display:'flex', flexDirection:'column'}}>
                
            <Form onChange={(data) => searchUsers(data)} />
            <DataTable columns={columns} data={tableData} />
            
            </div>
        </>
    );
};

export default Table;
