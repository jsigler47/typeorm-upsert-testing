import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Dog {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  name: string;

  @Column()
  age: number;

  @Column()
  breed: string;

  @Column()
  owner: string;
}
